import { LOAD_JOB_LISTINGS_SUCCESS, JobListingsActionTypes } from "./types";
import { JobListingSearchResponse } from "../../common/types";
import { Dispatch, Action, ActionCreator } from "redux";
import * as jobListingApi from "../../api/jobListingApi";

export const loadJobListingsSuccess: ActionCreator<Action> = (
  jobListings: JobListingSearchResponse
): JobListingsActionTypes => {
  return {
    type: LOAD_JOB_LISTINGS_SUCCESS,
    jobListings
  };
};

export const loadJobListings: any = () => {
  return async (dispatch: Dispatch) => {
    try {
      return jobListingApi.searchJobListings(null).then(jobListings => {
        dispatch(loadJobListingsSuccess(jobListings));
      });
    } catch (err) {
      throw new Error(err);
    }
  };
};
