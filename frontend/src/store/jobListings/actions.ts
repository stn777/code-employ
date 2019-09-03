import { LOAD_JOB_LISTINGS_SUCCESS, JobListingsActionTypes } from "./types";
import { JobListingSearchResponse } from "../../common/types";
import { Dispatch, Action, ActionCreator } from "redux";

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
      //TODO: Add service to communicate with API
      let jobListings: JobListingSearchResponse;
      dispatch(loadJobListingsSuccess(jobListings));
    } catch (err) {
      console.error(err);
    }
  };
};
