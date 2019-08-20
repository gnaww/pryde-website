from rest_framework import serializers
from rest_framework.fields import ListField
from django.contrib.auth import get_user_model
from .models import PUser, Project, Collaborator, TopicsProject, \
    DeliveryModeProject, ResearchInterestUser, File, AgeRangeUser, DeliveryModeUser, AgeRangeProject, UserEmailPreferences


class EmailPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmailPreferences
        exclude = ['id', 'user']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class FileShortSerializer(serializers.ModelSerializer):
    file_path = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ['file_path', 'file_name', 'pk']

    def get_file_path(self, obj):
        url = str(obj.file.url)
        return self.context.build_absolute_uri(url)


class DeliveryModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryModeProject
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicsProject
        fields = '__all__'


class MiniUserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = PUser
        fields = ['pk', 'first_name', 'last_name', 'affiliation', 'location', 'email', 'phone', 'website', 'type', 'role']

    def get_role(self, obj):
        return obj.get_role_display()


# Used for the project cards in the browse page
class ProjectShortSerializer(serializers.ModelSerializer):
    owner = MiniUserSerializer(many=False, read_only=True)
    status = serializers.SerializerMethodField()
    ageRanges = serializers.SerializerMethodField()
    researchTopics = serializers.SerializerMethodField()
    deliveryModes = serializers.SerializerMethodField()
    visible = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['pk', 'type', 'name', 'owner', 'status', 'summary', 'ageRanges', 'researchTopics', 'deliveryModes', 'datePosted', 'datePosted', 'visible']

    def get_status(self, obj):
        return obj.get_status_display()

    def get_ageRanges(self, obj):
        ages = AgeRangeProject.objects.filter(project=obj)
        return [age.ageRange for age in ages]

    def get_researchTopics(self, obj):
        topics = TopicsProject.objects.filter(project=obj)
        return [topic.researchTopic for topic in topics]

    def get_deliveryModes(self, obj):
        deliveryModes = DeliveryModeProject.objects.filter(project=obj)
        return [mode.deliveryMode for mode in deliveryModes]

    def get_visible(self, obj):
        if 'visible' in self.context:
            return self.context['visible']
        else:
            return True


class StringArrayField(ListField):
    def to_internal_value(self, data):
        return super().to_internal_value(data)


class UserSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    researchInterests = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()
    ageRanges = serializers.SerializerMethodField()
    deliveryModes = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        exclude = ['groups', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'password', 'user_permissions', 'username', 'type', 'over18']

    def get_projects(self, obj):
        projects = []
        collabs = Collaborator.objects.filter(collaborator=obj.pk, showProjectOnProfile=True)

        for collab in collabs:
            projects.append(ProjectShortSerializer(Project.objects.get(pk=collab.project.pk, isApproved=True)).data)

        owned_projects = Project.objects.filter(owner=obj.pk, isApproved=True)

        for project in owned_projects:
            projects.append(ProjectShortSerializer(project).data)

        return projects

    def get_role(self, obj):
        return obj.get_role_display()

    def get_researchInterests(self, obj):
        interests = ResearchInterestUser.objects.filter(user=obj)
        return [interest.researchInterest for interest in interests]

    def get_ageRanges(self, obj):
        ages = AgeRangeUser.objects.filter(user=obj)
        return [age.ageRange for age in ages]

    def get_deliveryModes(self, obj):
        modes = DeliveryModeUser.objects.filter(user=obj)
        return [mode.deliveryMode for mode in modes]

    def get_roles(self, obj):
        return obj.roles


class LoggedInUserSerializer(UserSerializer):
    def get_projects(self, obj):
        projects = []
        collabs = Collaborator.objects.filter(collaborator=obj.pk)

        for collab in collabs:
            if collab.showProjectOnProfile:
                projects.append(ProjectShortSerializer(Project.objects.get(pk=collab.project.pk, isApproved=True), context={'visible': True}).data)
            else:
                projects.append(ProjectShortSerializer(Project.objects.get(pk=collab.project.pk, isApproved=True), context={'visible': False}).data)

        owned_projects = Project.objects.filter(owner=obj.pk, isApproved=True)

        for project in owned_projects:
            projects.append(ProjectShortSerializer(project).data)

        return projects


# Used for the user cards in the browse page
class UserShortSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    numProjects = serializers.SerializerMethodField('num_projects')
    researchInterests = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['pk', 'type', 'profile_picture', 'first_name', 'last_name', 'role', 'affiliation', 'locatedAtCornell', 'locatedAtCCE', 'researchInterests', 'location', 'email', 'numProjects', 'date_joined']

    def get_role(self, obj):
        return obj.get_role_display()

    def num_projects(self, obj):
        total = 0
        collabs = Collaborator.objects.filter(collaborator=obj.pk, showProjectOnProfile=True)
        total += len(collabs)
        owned_projects = Project.objects.filter(owner=obj.pk, isApproved=True)
        total += len(owned_projects)

        return total

    def get_researchInterests(self, obj):
        interests = ResearchInterestUser.objects.filter(user=obj)
        return [interest.researchInterest for interest in interests]


class ProjectSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    owner = MiniUserSerializer(many=False, read_only=True)
    collaborators = serializers.SerializerMethodField()
    ageRanges = serializers.SerializerMethodField()
    researchTopics = serializers.SerializerMethodField()
    deliveryModes = serializers.SerializerMethodField()
    additionalFiles = serializers.SerializerMethodField('get_files')

    class Meta:
        model = Project
        exclude = ['isApproved', 'type']

    def get_collaborators(self, obj):
        collaborator_queryset = Collaborator.objects.filter(project=obj, showProjectOnProfile=True)
        collaborators = []
        for collaborator in collaborator_queryset:
            collaborators.append(UserShortSerializer(PUser.public_objects.get(pk=collaborator.collaborator.pk)).data)
        return collaborators

    def get_status(self, obj):
        return obj.get_status_display()

    def get_ageRanges(self, obj):
        ages = AgeRangeProject.objects.filter(project=obj)
        return [age.ageRange for age in ages]

    def get_researchTopics(self, obj):
        topics = TopicsProject.objects.filter(project=obj)
        return [topic.researchTopic for topic in topics]

    def get_deliveryModes(self, obj):
        deliveryModes = DeliveryModeProject.objects.filter(project=obj)
        return [mode.deliveryMode for mode in deliveryModes]

    def get_files(self, obj):
        if File.objects.filter(project=obj.pk).exists():
            serializer = FileShortSerializer(File.objects.filter(project=obj.pk), many=True, context=self.context.get('request'))
            return serializer.data
        return []


class CollaboratorSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Collaborator
        fields = ['pk', 'editPermission', 'deletePermission', 'editCollaboratorsPermission', 'email', 'first_name', 'last_name']

    def get_pk(self, obj):
        return PUser.public_objects.get(pk=obj.collaborator.pk).pk

    def get_first_name(self, obj):
        return PUser.public_objects.get(pk=obj.collaborator.pk).first_name

    def get_last_name(self, obj):
        return PUser.public_objects.get(pk=obj.collaborator.pk).last_name

    def get_email(self, obj):
        return PUser.public_objects.get(pk=obj.collaborator.pk).email


class CollaboratorSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PUser
        fields = ['pk', 'first_name', 'last_name', 'email']
