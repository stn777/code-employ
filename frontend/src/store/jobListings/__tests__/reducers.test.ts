import jobListingsReducer from "../reducers";
import * as actions from "../actions";
import {
  JobListingSearchResponse,
  JobListingList
} from "../../../common/types";
import { JobListingsState } from "../types";

it("should return a paginated list of jobListings when passed LOAD_JOB_LISTINGS_SUCCESS", () => {
  const initialState: JobListingsState = {
    jobListings: {
      recordCount: 0,
      items: []
    }
  };

  const jobListings: JobListingSearchResponse = {
    recordCount: 1,
    items: <JobListingList[]>[{ jobTitle: "A" }]
  };

  const action = actions.loadJobListingsSuccess(jobListings);
  const newState = jobListingsReducer(initialState, action);

  expect(newState.jobListings.recordCount).toEqual(1);
  expect(newState.jobListings.items[0].jobTitle).toEqual("A");
});
