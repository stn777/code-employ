import { combineReducers } from "redux";
import jobListings from "./jobListings/reducers";

const rootReducer = combineReducers({
  jobListings
});

export default rootReducer;
