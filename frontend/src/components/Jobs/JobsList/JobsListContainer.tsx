import * as React from "react";
import JobsList from "./JobsList";
import { connect } from "react-redux";
import { ApplicationState } from "../../../store";
import { JobListingSearchResponse } from "../../../common/types";

interface Props {
  jobListings: JobListingSearchResponse;
}

const JobsListContainer: React.SFC<Props> = ({ jobListings }) => {
  return <JobsList jobListings={jobListings} />;
};

const mapStateToProps = (state: ApplicationState) => state.jobListings;

export default connect(mapStateToProps)(JobsListContainer);
