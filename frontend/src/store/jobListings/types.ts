import { JobListingSearchResponse } from "../../common/types";

export const LOAD_JOB_LISTINGS_SUCCESS = "LOAD_JOB_LISTINGS_SUCCESS";

export interface JobListingsState {
  jobListings: JobListingSearchResponse;
}

export interface LoadJobListingsAction {
  type: typeof LOAD_JOB_LISTINGS_SUCCESS;
  jobListings: JobListingSearchResponse;
}

export type JobListingsActionTypes = LoadJobListingsAction;
