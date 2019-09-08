import * as React from "react";
import { ApplicationState } from "../../../store";
import * as jobsListingsFilterActions from "../../../store/jobListingFilter/actions";
import { connect } from "react-redux";
import { Dispatch } from "redux";
import { JobListingSearchFilter } from "../../../common/types";
import JobsListFilter from "./JobsListFilter";

interface Props {
  jobListingsFilter: JobListingSearchFilter;
  onUpdateFilter: (filter: JobListingSearchFilter) => void;
  onClearFilter: () => void;
}

const JobsListFilterContainer: React.SFC<Props> = ({
  jobListingsFilter,
  onUpdateFilter,
  onClearFilter
}) => {
  return (
    <JobsListFilter
      jobListingsFilter={jobListingsFilter}
      onUpdateFilter={onUpdateFilter}
      onClearFilter={onClearFilter}
    />
  );
};

const mapStateToProps = (state: ApplicationState) => state.jobListingsFilter;
const mapDispatchToProps = (dispatch: Dispatch) => {
  const actions = {
    onUpdateFilter: (filter: JobListingSearchFilter) =>
      dispatch(jobsListingsFilterActions.updateJobListingsFilter(filter)),
    onClearFilter: () =>
      dispatch(jobsListingsFilterActions.clearJobListingsFilter())
  };
  return actions;
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(JobsListFilterContainer);
