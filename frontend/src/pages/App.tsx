import * as React from "react";
import { HashRouter as Router, Route, Switch, Link } from "react-router-dom";
import HomePage from "./Home/HomePage";
import JobsList from "../components/Jobs/JobsList/JobsListContainer";

const App = () => (
  <Router>
    <nav>
      <Link to="/">Home</Link>
      <Link to="/Jobs">Jobs</Link>
    </nav>
    <Switch>
      <Route exact path="/" component={HomePage} />
      <Route exact path="/Jobs" component={JobsList} />
    </Switch>
  </Router>
);

export default App;
