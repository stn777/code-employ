import {
  JobListingsActionTypes,
  JobListingsState,
  LOAD_JOB_LISTINGS_SUCCESS
} from "./types";

const initialState: JobListingsState = {
  jobListings: {
    recordCount: 0,
    items: []
  }
};

export default function jobListingsReducer(
  state = initialState,
  action: JobListingsActionTypes
): JobListingsState {
  switch (action.type) {
    case LOAD_JOB_LISTINGS_SUCCESS:
      return {
        jobListings: action.jobListings
      };
    default:
      return state;
  }
}
