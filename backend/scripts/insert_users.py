import requests
import json
import random

researchTopics = ['Animal Science & Agriculture', 'Civic Engagement',
           'Diversity Equity & Inclusion', 'Education & Learning',
           'Environment & Sustainability', 'Families',
           'Health & Wellness', 'Peer Relationships',
           'Positive Youth Development', 'Policy Analysis',
           'Program Evaluation', 'Media & Technology',
           'Motivation', 'Nutrition', 'Risk Behavior',
           'Self & Identity', 'Science Technology Engineering & Math (STEM)',
           'Youth/Adult Relationships', 'Other']


deliveryModes = ['Afterschool', 'Camps', 'Clubs', 'Other']

ageRanges = ['Infants (0-1 year)', 'Toddlers (1-2 years)',
             'Toddlers (2-3 years)', 'Preschoolers (3-5 years)',
             'Early childhood (6-8 years)', 'Middle childhood (9-11 years)',
             'Young teens (12-14 years)', 'Teenagers (15-17 years)',
             'Young adults (18-24 years)']

firstName = ['John', 'Andy', 'Samantha', 'Lauren']
lastName = ['Smith', 'Jones', 'Johnson']

def pump_into_servers():
    url = 'http://localhost:8000/api/v1/rest-auth/registration/'
    headers = {
        'Content-Type': 'application/json',
        'cache-control': 'no-cache'
    }

    user1 = {
        "email": "test1@gmail.com",
        "password1": "password",
        "password2": "password",
        "first_name": random.choice(firstName),
        "last_name": random.choice(lastName),
        "role": 1,
        "displayRole": "Practice Focused Role",
        "affiliation": "cornell university",
        "location": "ithaca, NY",
        "phone": "+14432232248",
        "website": "http://www.google.com",
        "researchDescription": "i love doing research",
        "roles": ["string1", "string2", "string3"],
        "ageRanges": [random.choice(ageRanges), random.choice(ageRanges)],
        "researchInterests": [random.choice(researchTopics), random.choice(researchTopics)],
        "deliveryModes": [random.choice(deliveryModes), random.choice(deliveryModes)],
        "researchNeeds": "this is a research need!",
        "evaluationNeeds": "this is an evaluation need!",
        "locatedAtCornell": False,
        "locatedAtCCE": False
    }

    user2 = {
        "email": "test2@gmail.com",
        "password1": "password",
        "password2": "password",
        "first_name": random.choice(firstName),
        "last_name": random.choice(lastName),
        "role": 1,
        "displayRole": "Practice Focused Role",
        "affiliation": "cornell university",
        "location": "ithaca, NY",
        "phone": "+14432232248",
        "website": "http://www.google.com",
        "researchDescription": "i love doing research",
        "roles": ["string1", "string2", "string3"],
        "ageRanges": [random.choice(ageRanges), random.choice(ageRanges)],
        "researchInterests": [random.choice(researchTopics), random.choice(researchTopics)],
        "deliveryModes": [random.choice(deliveryModes), random.choice(deliveryModes)],
        "researchNeeds": "this is a research need!",
        "evaluationNeeds": "this is an evaluation need!",
        "locatedAtCornell": False,
        "locatedAtCCE": False
    }

    user3 = {
        "email": "test3@gmail.com",
        "password1": "password",
        "password2": "password",
        "first_name": random.choice(firstName),
        "last_name": random.choice(lastName),
        "role": 1,
        "displayRole": "Other CCE Role",
        "affiliation": "cornell university",
        "location": "ithaca, NY",
        "phone": "+14432232248",
        "website": "http://www.google.com",
        "researchDescription": "i love doing research",
        "roles": ["string1", "string2", "string3"],
        "ageRanges": [random.choice(ageRanges), random.choice(ageRanges)],
        "researchInterests": [random.choice(researchTopics), random.choice(researchTopics)],
        "deliveryModes": [random.choice(deliveryModes), random.choice(deliveryModes)],
        "researchNeeds": "this is a research need!",
        "evaluationNeeds": "this is an evaluation need!",
        "locatedAtCornell": False,
        "locatedAtCCE": True
    }

    user4 = {
        "email": "test4@gmail.com",
        "password1": "password",
        "password2": "password",
        "first_name": random.choice(firstName),
        "last_name": random.choice(lastName),
        "role": 1,
        "displayRole": "Research Focused Role",
        "affiliation": "cornell university",
        "location": "ithaca, NY",
        "phone": "+14432232248",
        "website": "http://www.google.com",
        "researchDescription": "i love doing research",
        "roles": ["string1", "string2", "string3"],
        "ageRanges": [random.choice(ageRanges), random.choice(ageRanges)],
        "researchInterests": [random.choice(researchTopics), random.choice(researchTopics)],
        "deliveryModes": [random.choice(deliveryModes), random.choice(deliveryModes)],
        "researchNeeds": "this is a research need!",
        "evaluationNeeds": "this is an evaluation need!",
        "locatedAtCornell": True,
        "locatedAtCCE": False
    }

    user5 = {
        "email": "test5@gmail.com",
        "password1": "password",
        "password2": "password",
        "first_name": random.choice(firstName),
        "last_name": random.choice(lastName),
        "role": 1,
        "displayRole": "Research Focused Role",
        "affiliation": "cornell university",
        "location": "ithaca, NY",
        "phone": "+14432232248",
        "website": "http://www.google.com",
        "researchDescription": "i love doing research",
        "roles": ["string1", "string2", "string3"],
        "ageRanges": [random.choice(ageRanges), random.choice(ageRanges)],
        "researchInterests": [random.choice(researchTopics), random.choice(researchTopics)],
        "deliveryModes": [random.choice(deliveryModes), random.choice(deliveryModes)],
        "researchNeeds": "this is a research need!",
        "evaluationNeeds": "this is an evaluation need!",
        "locatedAtCornell": True,
        "locatedAtCCE": False
    }

    user6 = {
        "email": "test6@gmail.com",
        "password1": "password",
        "password2": "password",
        "first_name": random.choice(firstName),
        "last_name": random.choice(lastName),
        "role": 2,
        "displayRole": "Research Focused Role",
        "affiliation": "cornell university",
        "location": "ithaca, NY",
        "phone": "+14432232248",
        "website": "http://www.google.com",
        "researchDescription": "i love doing research",
        "roles": ["string1", "string2", "string3"],
        "ageRanges": [random.choice(ageRanges), random.choice(ageRanges)],
        "researchInterests": [random.choice(researchTopics), random.choice(researchTopics)],
        "deliveryModes": [random.choice(deliveryModes), random.choice(deliveryModes)],
        "researchNeeds": "this is a research need!",
        "evaluationNeeds": "this is an evaluation need!",
        "locatedAtCornell": True,
        "locatedAtCCE": False
    }

    user7 = {
        "email": "test7@gmail.com",
        "password1": "password",
        "password2": "password",
        "first_name": random.choice(firstName),
        "last_name": random.choice(lastName),
        "role": 2,
        "displayRole": "Research Focused Role",
        "affiliation": "cornell university",
        "location": "ithaca, NY",
        "phone": "+14432232248",
        "website": "http://www.google.com",
        "researchDescription": "i love doing research",
        "roles": ["string1", "string2", "string3"],
        "ageRanges": [random.choice(ageRanges), random.choice(ageRanges)],
        "researchInterests": [random.choice(researchTopics), random.choice(researchTopics)],
        "deliveryModes": [random.choice(deliveryModes), random.choice(deliveryModes)],
        "researchNeeds": "this is a research need!",
        "evaluationNeeds": "this is an evaluation need!",
        "locatedAtCornell": True,
        "locatedAtCCE": False
    }

    user8 = {
        "email": "test8@gmail.com",
        "password1": "password",
        "password2": "password",
        "first_name": random.choice(firstName),
        "last_name": random.choice(lastName),
        "role": 2,
        "displayRole": "Research Focused Role",
        "affiliation": "cornell university",
        "location": "ithaca, NY",
        "phone": "+14432232248",
        "website": "http://www.google.com",
        "researchDescription": "i love doing research",
        "roles": ["string1", "string2", "string3"],
        "ageRanges": [random.choice(ageRanges), random.choice(ageRanges)],
        "researchInterests": [random.choice(researchTopics), random.choice(researchTopics)],
        "deliveryModes": [random.choice(deliveryModes), random.choice(deliveryModes)],
        "researchNeeds": "this is a research need!",
        "evaluationNeeds": "this is an evaluation need!",
        "locatedAtCornell": True,
        "locatedAtCCE": False
    }

    user9 = {
        "email": "test9@gmail.com",
        "password1": "password",
        "password2": "password",
        "first_name": random.choice(firstName),
        "last_name": random.choice(lastName),
        "role": 2,
        "displayRole": "Research Focused Role",
        "affiliation": "cornell university",
        "location": "ithaca, NY",
        "phone": "+14432232248",
        "website": "http://www.google.com",
        "researchDescription": "i love doing research",
        "roles": ["string1", "string2", "string3"],
        "ageRanges": [random.choice(ageRanges), random.choice(ageRanges)],
        "researchInterests": [random.choice(researchTopics), random.choice(researchTopics)],
        "deliveryModes": [random.choice(deliveryModes), random.choice(deliveryModes)],
        "researchNeeds": "this is a research need!",
        "evaluationNeeds": "this is an evaluation need!",
        "locatedAtCornell": True,
        "locatedAtCCE": False
    }

    user10 = {
        "email": "test10@gmail.com",
        "password1": "password",
        "password2": "password",
        "first_name": random.choice(firstName),
        "last_name": random.choice(lastName),
        "role": 2,
        "displayRole": "Research Focused Role",
        "affiliation": "Rutgers University",
        "location": "New Brunswick, NJ",
        "phone": "+14432232248",
        "website": "http://www.google.com",
        "researchDescription": "i love doing research",
        "roles": ["string1", "string2", "string3"],
        "ageRanges": [random.choice(ageRanges), random.choice(ageRanges)],
        "researchInterests": [random.choice(researchTopics), random.choice(researchTopics)],
        "deliveryModes": [random.choice(deliveryModes), random.choice(deliveryModes)],
        "researchNeeds": "this is a research need!",
        "evaluationNeeds": "this is an evaluation need!",
        "locatedAtCornell": False,
        "locatedAtCCE": False
    }

    users = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10]

    for user in users:
        response = requests.request("POST", url, data=json.dumps(user), headers=headers)
        print(response)

pump_into_servers()

