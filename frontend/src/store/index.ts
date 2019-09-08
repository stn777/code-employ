import { combineReducers } from "redux";
import jobListings from "./jobListings/reducers";
import { JobListingsState } from "./jobListings/types";
import jobListingsFilter from "./jobListingFilter/reducers";
import { JobListingsFilterState } from "./jobListingFilter/types";
import apiStatus from "./apiStatus/reducers";
import { ApiStatusState } from "./apiStatus/types";

export interface ApplicationState {
  jobListings: JobListingsState;
  jobListingsFilter: JobListingsFilterState;
  apiStatus: ApiStatusState;
}

export const rootReducer = combineReducers<ApplicationState>({
  jobListings,
  jobListingsFilter,
  apiStatus
});

export default rootReducer;
