import * as React from "react";
import { Route, Switch, Link } from "react-router-dom";
import { Hello } from "./Hello";

const App = () => (
  <div>
    <nav>
      <Link to="/">Home</Link>
      <Link to="/Two">Two</Link>
    </nav>
    <Switch>
      <Route exact path="/" component={Hello} />
      <Route exact path="/Two" component={Hello} />
    </Switch>
  </div>
);

export default App;
