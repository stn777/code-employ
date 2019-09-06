import * as React from "react";
import * as ReactDOM from "react-dom";

import { Provider } from "react-redux";
import App from "./pages/App";
import configureStore from "./store/configureStore";
import { loadJobListings } from "./store/jobListings/actions";
import { JobListingSearchFilter } from "./common/types";

const store = configureStore();
const filter = {} as JobListingSearchFilter;
filter.keyword = "hi";
store.dispatch(loadJobListings(filter));

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("app")
);
