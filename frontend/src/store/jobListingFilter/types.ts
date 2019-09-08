import { JobListingSearchFilter } from "../../common/types";

export const UPDATE_JOB_LISTINGS_FILTER = "UPDATE_JOB_LISTINGS_FILTER";
export const CLEAR_JOB_LISTINGS_FILTER = "CLEAR_JOB_LISTINGS_FILTER";

export interface JobListingsFilterState {
  jobListingsFilter: JobListingSearchFilter;
}

export interface UpdateJobListingsFilterAction {
  type: typeof UPDATE_JOB_LISTINGS_FILTER;
  filter: JobListingSearchFilter;
}

export interface ClearJobListingsFilterAction {
  type: typeof CLEAR_JOB_LISTINGS_FILTER;
}

export type JobListingsFilterActionTypes =
  | UpdateJobListingsFilterAction
  | ClearJobListingsFilterAction;
