import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import Homepage from './pages/Homepage';
import Browse from './pages/Browse';
import Login from './pages/Login';
import CreateProfile from './pages/CreateProfile/CreateProfile';
import CreateProject from './pages/CreateProject/CreateProject';
import Profile from './pages/Profile';
import Project from './pages/Project';
import EditProfile from './pages/EditProfile';
import EditProject from './pages/EditProject';
import PageNotFound from './pages/PageNotFound';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import styles from './App.module.css';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            loggedIn: false
        };
    }

    setLoggedIn = () => {
        this.setState({ loggedIn: true });
    }

    setLoggedOut = () => {
        this.setState({ loggedIn: false });
    }

    componentDidMount() {
        if (localStorage.getItem("pryde_key")) {
            this.setState({ loggedIn: true });
        }
    }

    render() {
        return (
            <Router>
                <div className={styles.wrapper}>
                    <Navbar loggedIn={this.state.loggedIn} setLoggedOut={this.setLoggedOut} />
                    <Switch>
                        <Route path="/" exact component={Homepage} />
                        <Route path="/browse" component={Browse} />
                        <Route path="/login" exact render={renderProps => (
                            localStorage.getItem("pryde_key") ? <Redirect to="/" /> : <Login setLoggedIn={this.setLoggedIn} {...renderProps} />
                        )} />
                        <Route path="/signup" exact render={renderProps => (
                            localStorage.getItem("pryde_key") ? <Redirect to="/" /> : <CreateProfile {...renderProps} />
                        )} />
                        <Route path="/myprofile" exact render={renderProps => (
                            !localStorage.getItem("pryde_key") ? <Redirect to="/" /> : <Profile {...renderProps} />
                        )} />
                        <Route path="/submit" exact component={CreateProject} />
                        <Route path="/user/:id" component={Profile} />
                        <Route path="/project/:id" component={Project} />
                        <Route path="/editprofile" exact component={EditProfile} />
                        <Route path="/editproject" exact component={EditProject} />
                        <Route component={PageNotFound} />
                    </Switch>
                    <Footer />
                </div>
            </Router>
        );
    }
}

export default App;
