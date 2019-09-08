import { createStore } from "redux";
import { rootReducer, ApplicationState } from "../..";
import * as actions from "../actions";
import { JobListingSearchFilter } from "../../../common/types";

it("should handle updating the Job Listings filter", () => {
  const store = createStore(rootReducer);
  const jobListingFilter = {
    keyword: "A"
  } as JobListingSearchFilter;

  const action = actions.updateJobListingsFilter(jobListingFilter);
  store.dispatch(action);

  const newState = store.getState().jobListingsFilter.jobListingsFilter;
  expect(newState).toEqual(jobListingFilter);
});

it("should handle clearing the Job Listings filter", () => {
  const initialState = {
    jobListingsFilter: {
      jobListingsFilter: {
        keyword: "A"
      }
    }
  };

  const store = createStore(rootReducer, initialState as ApplicationState);
  const action = actions.clearJobListingsFilter();
  store.dispatch(action);

  const newState = store.getState().jobListingsFilter.jobListingsFilter;
  expect(newState.keyword).toEqual("");
});
