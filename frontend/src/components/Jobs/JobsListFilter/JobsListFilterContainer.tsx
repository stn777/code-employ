import * as React from "react";
import { ApplicationState } from "../../../store";
import * as filterActions from "../../../store/jobListingFilter/actions";
import { connect } from "react-redux";
import { Dispatch } from "redux";
import { JobListingSearchFilter } from "../../../common/types";
import JobsListFilter from "./JobsListFilter";

interface Props {
  jobListingsFilter: JobListingSearchFilter;
  updateFilter: (filter: JobListingSearchFilter) => void;
  clearFilter: () => void;
}

const JobsListFilterContainer: React.SFC<Props> = ({
  jobListingsFilter,
  updateFilter,
  clearFilter
}) => {
  const handleChange = (e: any) => {
    const { name, value } = e.target;
    updateFilter({
      ...jobListingsFilter,
      [name]: value
    });
  };
  return (
    <JobsListFilter
      jobListingsFilter={jobListingsFilter}
      onUpdateFilter={handleChange}
      onClearFilter={clearFilter}
    />
  );
};

const mapStateToProps = (state: ApplicationState) => state.jobListingsFilter;
const mapDispatchToProps = (dispatch: Dispatch) => {
  const actions = {
    updateFilter: (filter: JobListingSearchFilter) =>
      dispatch(filterActions.updateJobListingsFilter(filter)),
    clearFilter: () => dispatch(filterActions.clearJobListingsFilter())
  };
  return actions;
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(JobsListFilterContainer);
