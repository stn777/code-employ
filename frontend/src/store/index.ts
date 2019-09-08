import { combineReducers } from "redux";
import jobListings from "./jobListings/reducers";
import { JobListingsState } from "./jobListings/types";
import jobListingsFilter from "./jobListingFilter/reducers";
import { JobListingsFilterState } from "./jobListingFilter/types";

export interface ApplicationState {
  jobListings: JobListingsState;
  jobListingsFilter: JobListingsFilterState;
}

export const rootReducer = combineReducers<ApplicationState>({
  jobListings,
  jobListingsFilter
});

export default rootReducer;
