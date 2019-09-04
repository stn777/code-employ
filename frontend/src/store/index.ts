import { combineReducers, Reducer } from "redux";
import jobListings from "./jobListings/reducers";
import { JobListingsState } from "./jobListings/types";

export interface ApplicationState {
  jobListings: JobListingsState;
}

export const rootReducer = combineReducers<ApplicationState>({
  jobListings
});

export default rootReducer;
