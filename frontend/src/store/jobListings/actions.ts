import { LOAD_JOB_LISTINGS_SUCCESS, JobListingsActionTypes } from "./types";
import {
  JobListingSearchResponse,
  JobListingSearchFilter
} from "../../common/types";
import { Dispatch } from "redux";
import * as jobListingApi from "../../api/jobListingApi";

export const loadJobListingsSuccess = (
  jobListings: JobListingSearchResponse
): JobListingsActionTypes => {
  return {
    type: LOAD_JOB_LISTINGS_SUCCESS,
    jobListings
  };
};

export const loadJobListings: any = (filter: JobListingSearchFilter) => {
  return async (dispatch: Dispatch) => {
    try {
      return jobListingApi.searchJobListings(filter).then(jobListings => {
        dispatch(loadJobListingsSuccess(jobListings));
      });
    } catch (err) {
      throw new Error(err);
    }
  };
};
