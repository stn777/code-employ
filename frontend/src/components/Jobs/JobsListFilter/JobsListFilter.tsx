import * as React from "react";
import { JobListingSearchFilter } from "../../../common/types";

interface Props {
  jobsListingsFilter: JobListingSearchFilter;
  onUpdateFilter: (filter: JobListingSearchFilter) => void;
  onClearFilter: () => void;
}

const JobsListFilter: React.SFC<Props> = () => {
  return <div>Filter</div>;
};

export default JobsListFilter;
