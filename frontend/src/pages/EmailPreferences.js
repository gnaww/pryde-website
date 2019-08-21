import React, { Component } from 'react';
import styles from '../styles/Login.module.css';
import api from '../services/api';
import { PractitionerInformation } from './CreateProfile/FormContent';
import { AnswerTypes, getCheckboxQuestion, getCheckedValuesArray, getResearchTopicsQuestion } from '../components/QAComponents';
import { convertArray, convertResearchTopics, formatPreferencesArray } from '../services/util';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';

const userPreferenceQuestions = [
    {
        questionText: "Select user age ranges",
        answer: {
            type: AnswerTypes.Checkbox,
            options: PractitionerInformation.AgeGroups,
            key: "userAgeRanges"
        }
    },
    {
        questionText:
            "Select user delivery modes",
        answer: {
            type: AnswerTypes.Checkbox,
            options:
                PractitionerInformation.ProgramDeliveryModes,
            key: "userDeliveryModes"
        }
    },
    {
        questionText:
            "Select user research interests",
        answer: {
            type: AnswerTypes.ResearchTopics,
            options: PractitionerInformation.ResearchTopics,
            key: "userResearchInterests"
        }
    }
];

const projectPreferenceQuestions = [
    {
        questionText: "Select project age ranges",
        answer: {
            type: AnswerTypes.Checkbox,
            options: PractitionerInformation.AgeGroups,
            key: "projectAgeRanges"
        }
    },
    {
        questionText:
            "Select project delivery modes",
        answer: {
            type: AnswerTypes.Checkbox,
            options:
                PractitionerInformation.ProgramDeliveryModes,
            key: "projectDeliveryModes"
        }
    },
    {
        questionText:
            "Select project research topics",
        answer: {
            type: AnswerTypes.ResearchTopics,
            options: PractitionerInformation.ResearchTopics,
            key: "projectResearchTopics"
        }
    }
];

class EmailPreferences extends Component {
    constructor(props) {
        super(props);
        this.state = {
            userAgeRanges: getCheckedValuesArray(PractitionerInformation.AgeGroups),
            userDeliveryModes: getCheckedValuesArray(PractitionerInformation.ProgramDeliveryModes),
            userResearchInterests: getCheckedValuesArray(PractitionerInformation.ResearchTopics),
            projectAgeRanges: getCheckedValuesArray(PractitionerInformation.AgeGroups),
            projectDeliveryModes: getCheckedValuesArray(PractitionerInformation.ProgramDeliveryModes),
            projectResearchTopics: getCheckedValuesArray(PractitionerInformation.ResearchTopics),
            tabValue: 0,
            successMessage: '',
            errorMessage: ''
        };
    }

    setValues = (key, index, text) => {
        let copy = Array.from(this.state[key]);

        if (text !== null) {
            copy[index].other = text;
        }
        else {
            copy[index].checked = !copy[index].checked;
            copy[index].other = "";
        }

        this.setState({
            [key]: copy
        });
    }

    getQAComponent = (qa, index) => {
        return (
            <div className={styles.question} key={index}>
                { getCheckboxQuestion(qa, this.setValues, this.state, false) }
                { getResearchTopicsQuestion(qa, this.setValues, this.state, false) }
            </div>
        );
    }

    changeTab = (event, newValue) => {
        this.setState({ tabValue: newValue });
    }

    savePreferences = () => {
        this.setState({ successMessage: "", errorMessage: "" });

        const { userAgeRanges, userDeliveryModes, userResearchInterests, projectAgeRanges, projectDeliveryModes, projectResearchTopics } = this.state;

        let preferences = [].concat(
            formatPreferencesArray(userAgeRanges, projectAgeRanges, "ageRange", "ageRange"),
            formatPreferencesArray(userDeliveryModes, projectDeliveryModes, "deliveryMode", "deliveryMode"),
            formatPreferencesArray(userResearchInterests, projectResearchTopics, "researchInterest", "researchTopic")
        );

        if (preferences.length !== 0) {
            api.updateEmailPreferences(preferences)
                .then(response => {
                    this.setState({ successMessage: "Email preferences successfully saved." });
                })
                .catch(error => {
                    console.log(error);
                    this.setState({ errorMessage: Object.values(error.response.data)[0] });
                });
        } else {
            this.setState({ errorMessage: "At least one preference must be selected." });
        }
    }

    unsubscribe = () => {
        this.setState({ successMessage: "", errorMessage: "" });
        api.unsubscribe()
            .then(response => {
                if (response) {
                    this.setState({
                        successMessage: "Successfully unsubscribed from all emails.",
                        userAgeRanges: getCheckedValuesArray(PractitionerInformation.AgeGroups),
                        userDeliveryModes: getCheckedValuesArray(PractitionerInformation.ProgramDeliveryModes),
                        userResearchInterests: getCheckedValuesArray(PractitionerInformation.ResearchTopics),
                        projectAgeRanges: getCheckedValuesArray(PractitionerInformation.AgeGroups),
                        projectDeliveryModes: getCheckedValuesArray(PractitionerInformation.ProgramDeliveryModes),
                        projectResearchTopics: getCheckedValuesArray(PractitionerInformation.ResearchTopics)
                    });
                }
            })
            .catch(error => {
                console.log(error);
                this.setState({ errorMessage: Object.values(error.response.data)[0] });
            });
    }

    initializePreferences = preferences => {
        let initialUserAgeRanges = [];
        let initialUserDeliveryModes = [];
        let initialUserResearchInterests = [];
        let initialProjectAgeRanges = [];
        let initialProjectDeliveryModes = [];
        let initialProjectResearchTopics = [];

        preferences.forEach(preference => {
            // project preference
            if (preference.type === "1") {
                if (preference.preferenceName === "ageRange") {
                    initialProjectAgeRanges.push(preference.preferenceValue);
                } else if (preference.preferenceName === "deliveryMode") {
                    initialProjectDeliveryModes.push(preference.preferenceValue);
                } else if (preference.preferenceName === "researchTopic") {
                    initialProjectResearchTopics.push(preference.preferenceValue);
                }
            } else { // user preference
                if (preference.preferenceName === "ageRange") {
                    initialUserAgeRanges.push(preference.preferenceValue);
                } else if (preference.preferenceName === "deliveryMode") {
                    initialUserDeliveryModes.push(preference.preferenceValue);
                } else if (preference.preferenceName === "researchInterest") {
                    initialUserResearchInterests.push(preference.preferenceValue);
                }
            }
        });

        initialUserAgeRanges = convertArray(initialUserAgeRanges, PractitionerInformation.AgeGroups);
        initialUserDeliveryModes = convertArray(initialUserDeliveryModes, PractitionerInformation.ProgramDeliveryModes);
        initialUserResearchInterests = convertResearchTopics(initialUserResearchInterests, PractitionerInformation.ResearchTopics);
        initialProjectAgeRanges = convertArray(initialProjectAgeRanges, PractitionerInformation.AgeGroups);
        initialProjectDeliveryModes = convertArray(initialProjectDeliveryModes, PractitionerInformation.ProgramDeliveryModes);
        initialProjectResearchTopics = convertResearchTopics(initialProjectResearchTopics, PractitionerInformation.ResearchTopics);

        this.setState({
            userAgeRanges: initialUserAgeRanges,
            userDeliveryModes: initialUserDeliveryModes,
            userResearchInterests: initialUserResearchInterests,
            projectAgeRanges: initialProjectAgeRanges,
            projectDeliveryModes: initialProjectDeliveryModes,
            projectResearchTopics: initialProjectResearchTopics
        });
    }

    clearUserPreferences = () => {
        this.setState({
            userAgeRanges: getCheckedValuesArray(PractitionerInformation.AgeGroups),
            userDeliveryModes: getCheckedValuesArray(PractitionerInformation.ProgramDeliveryModes),
            userResearchInterests: getCheckedValuesArray(PractitionerInformation.ResearchTopics),
        });
    }

    clearProjectPreferences = () => {
        this.setState({
            projectAgeRanges: getCheckedValuesArray(PractitionerInformation.AgeGroups),
            projectDeliveryModes: getCheckedValuesArray(PractitionerInformation.ProgramDeliveryModes),
            projectResearchTopics: getCheckedValuesArray(PractitionerInformation.ResearchTopics)
        });
    }

    componentDidMount() {
        document.title = "PRYDE Connect | Email Preferences";
        api.getEmailPreferences()
            .then(preferences => {
                if (preferences.length !== 0) {
                    this.initializePreferences(preferences);
                }
            });
    }

    render() {
        return (
            <div className={styles.emailPreferenceWrapper}>
                <h1 className={styles.title}>
                    Update email preferences
                </h1>
                <h2 className={styles.description}>
                    Selecting a preference means you will be opting into monthly emails notifying you of new users and/or projects that match your selected preferences. You may unsubscribe at any time.
                </h2>
                {
                    this.state.successMessage &&
                    <p className={styles.successMessage}>{this.state.successMessage}</p>
                }
                {
                    this.state.errorMessage &&
                    <p className={styles.errorMessage}>{this.state.errorMessage}</p>
                }
                <div className={styles.buttonWrapper}>
                    <button className={styles.update} onClick={this.savePreferences}>
                        UPDATE PREFERENCES
                    </button>
                    <button className={styles.unsubscribe} onClick={this.unsubscribe}>
                        UNSUBSCRIBE FROM ALL EMAILS
                    </button>
                </div>
                <Tabs className={styles.tabMenu}
                    value={this.state.tabValue}
                    indicatorColor="primary"
                    textColor="primary"
                    onChange={this.changeTab}
                    variant="fullWidth"
                >
                    <Tab disableRipple label="User Email Preferences" />
                    <Tab disableRipple label="Project Email Preferences" />
                </Tabs>
                <div className={styles.center}>
                    <button
                        className={styles.unsubscribe}
                        onClick={() => {
                            if (this.state.tabValue === 0) {
                                this.clearUserPreferences();
                            } else {
                                this.clearProjectPreferences();
                            }
                        }}
                    >
                        CLEAR { this.state.tabValue === 0 ? "USER" : "PROJECT" } PREFERENCES
                    </button>
                </div>
                {
                    this.state.tabValue === 0 ?
                        <>
                            <div className={styles.questionsWrapper}>
                                {
                                    this.getQAComponent(userPreferenceQuestions[0], 0)
                                }
                                {
                                    this.getQAComponent(userPreferenceQuestions[1], 1)
                                }
                            </div>
                            {
                                this.getQAComponent(userPreferenceQuestions[2], 2)
                            }
                        </>
                    :
                        <>
                            <div className={styles.questionsWrapper}>
                                {
                                    this.getQAComponent(projectPreferenceQuestions[0], 0)
                                }
                                {
                                    this.getQAComponent(projectPreferenceQuestions[1], 1)
                                }
                            </div>
                            {
                                this.getQAComponent(projectPreferenceQuestions[2], 2)
                            }
                        </>
                }
            </div>
        );
    }
}

export default EmailPreferences;