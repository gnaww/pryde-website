import React, { Component } from 'react';
import CreateProject from './CreateProject/CreateProject';
import { PractitionerInformation } from './CreateProfile/FormContent';
import api from '../services/api';
import { popState } from '../services/localStorage';
import { convertArray, convertResearchTopics } from '../services/util';

const formatInputbox = value => ({
    option: value,
    other: ""
});

const STATUSES = ["Completed", "In Progress", "Not Started"];

class EditProject extends Component {
    constructor(props) {
        super(props);
        this.state = {
        };
    }

    async componentDidMount() {
        try {
            let editProjectData = Object.assign({}, popState("projectData"));
            delete editProjectData.invalidProject;
            delete editProjectData.editPermission;
            delete editProjectData.deletePermission;
            delete editProjectData.isCollaborator;
            delete editProjectData.showProjectOnProfile;
            delete editProjectData.owner;
            delete editProjectData.datePosted;
            editProjectData.name = formatInputbox(editProjectData.name);
            editProjectData.alternateLocation = formatInputbox(editProjectData.alternateLocation);

            let collaborators = await api.getProjectCollaborators(editProjectData.id)
            editProjectData.collaborators = collaborators.map(elt => ({ ...elt }));
            editProjectData.initialCollaborators = collaborators.map(elt => ({ ...elt }));

            editProjectData.timeline = formatInputbox(editProjectData.timeline);
            editProjectData.commitmentLength = formatInputbox(editProjectData.commitmentLength);
            editProjectData.incentives = formatInputbox(editProjectData.incentives);
            if (Object.entries(editProjectData.alternateContact).length === 0) {
                editProjectData.alternateContact = {
                    first_name: "",
                    last_name: "",
                    email: "",
                    phone: "",
                    website: ""
                };
            }
            editProjectData.alternateContact.phone = editProjectData.alternateContact.phone ? editProjectData.alternateContact.phone.slice(2) : "";
            editProjectData.alternateContact.website = editProjectData.alternateContact.website ? editProjectData.alternateContact.website.replace(/(^\w+:|^)\/\//, '') : "";
            editProjectData.status = STATUSES.indexOf(editProjectData.status) + 1;
            editProjectData.researchTopics = convertResearchTopics(editProjectData.researchTopics, PractitionerInformation.ResearchTopics);
            editProjectData.ageRanges = convertArray(editProjectData.ageRanges, PractitionerInformation.AgeGroups);
            editProjectData.deliveryModes = convertArray(editProjectData.deliveryModes, PractitionerInformation.ProgramDeliveryModes);
            editProjectData.additionalFiles = editProjectData.additionalFiles.map(file => {
                return [file.pk, file.file_name]
            });
            editProjectData.initialAdditionalFiles = editProjectData.additionalFiles.map(elt => elt);
            this.setState({ ...editProjectData });
        } catch (err) {
            console.log(err);
            alert("Something went wrong while loading the edit project page. Please close this tab and try again.");
        }
    }

    render() {
        if (Object.entries(this.state).length === 0) {
            return <CreateProject editProjectData={null} editing={true} location={this.props.location} />
        } else {
            return <CreateProject editProjectData={this.state} editing={true} location={this.props.location} />
        }
    }
}

export default EditProject;
