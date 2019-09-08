import {
  UPDATE_JOB_LISTINGS_FILTER,
  CLEAR_JOB_LISTINGS_FILTER,
  JobListingsFilterActionTypes
} from "./types";
import { JobListingSearchFilter } from "../../common/types";

export const updateJobListingsFilter = (
  filter: JobListingSearchFilter
): JobListingsFilterActionTypes => {
  return {
    type: UPDATE_JOB_LISTINGS_FILTER,
    filter
  };
};

export const clearJobListingsFilter = (): JobListingsFilterActionTypes => {
  return {
    type: CLEAR_JOB_LISTINGS_FILTER
  };
};
