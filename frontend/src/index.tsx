import * as React from "react";
import * as ReactDOM from "react-dom";
import { HashRouter as Router } from "react-router-dom";
import { Provider } from "react-redux";
import App from "./components/App";
import configureStore from "./store/configureStore";

const store = configureStore();

ReactDOM.render(
  <Provider store={store}>
    <Router>
      <App />,
    </Router>
  </Provider>,
  document.getElementById("app")
);
