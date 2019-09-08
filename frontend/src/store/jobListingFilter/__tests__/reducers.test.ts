import jobListingsFilterReducer from "../reducers";
import * as actions from "../actions";
import { JobListingSearchFilter } from "../../../common/types";
import { JobListingsFilterState } from "../types";

it("should return an updated jobListingSearchFilter when passed UPDATE_JOB_LISTINGS_FILTER", () => {
  const initialState: JobListingsFilterState = {
    jobListingsFilter: {
      keyword: "A"
    } as JobListingSearchFilter
  };

  const jobListingsFilter = {
    keyword: "B"
  } as JobListingSearchFilter;

  const action = actions.updateJobListingsFilter(jobListingsFilter);
  const newState = jobListingsFilterReducer(initialState, action);

  expect(newState.jobListingsFilter.keyword).toEqual("B");
});

it("should return an empty jobListingSearchFilter when passed CLEAR_JOB_LISTINGS_FILTER", () => {
  const initialState: JobListingsFilterState = {
    jobListingsFilter: {
      keyword: "A"
    } as JobListingSearchFilter
  };

  const action = actions.clearJobListingsFilter();
  const newState = jobListingsFilterReducer(initialState, action);

  expect(newState.jobListingsFilter.keyword).toBeUndefined();
});
