import * as React from "react";
import JobsList from "./JobsList";
import { connect } from "react-redux";
import { ApplicationState } from "../../../store";
import * as jobListingActions from "../../../store/jobListings/actions";
import { Dispatch } from "redux";
import {
  JobListingSearchResponse,
  JobListingSearchFilter
} from "../../../common/types";

interface Props {
  jobListings: JobListingSearchResponse;
  loadJobListings: (filter: JobListingSearchFilter) => Promise<void>;
}

const JobsListContainer: React.SFC<Props> = ({
  jobListings,
  loadJobListings
}) => {
  let filter: JobListingSearchFilter;
  React.useEffect(() => {
    loadJobListings(filter).catch(error => {
      console.log(error);
    });
  }, []);
  return <JobsList jobListings={jobListings} />;
};

const mapStateToProps = (state: ApplicationState) => state.jobListings;
const mapDispatchtoProps = (dispatch: Dispatch) => {
  const actions = {
    loadJobListings: (filter: JobListingSearchFilter) =>
      dispatch(jobListingActions.loadJobListings(filter))
  };
  return actions;
};

export default connect(
  mapStateToProps,
  mapDispatchtoProps
)(JobsListContainer);
