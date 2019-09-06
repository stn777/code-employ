import { createStore } from "redux";
import { rootReducer } from "../..";
import * as actions from "../actions";
import { JobListing, JobListingSearchResponse } from "../../../common/types";

it("Should handle loading Job Listings", () => {
  const store = createStore(rootReducer);
  const jobListings: JobListingSearchResponse = {
    recordCount: 1,
    items: <JobListing[]>[{ jobTitle: "A" }]
  };

  const action = actions.loadJobListingsSuccess(jobListings);
  store.dispatch(action);

  const newState = store.getState().jobListings.jobListings;
  expect(newState).toEqual(jobListings);
});
