import * as React from "react";
import { JobListingSearchFilter } from "../../../common/types";
import { Paper, Typography, Grid } from "@material-ui/core";

interface Props {
  jobListingsFilter: JobListingSearchFilter;
  onUpdateFilter: (filter: JobListingSearchFilter) => void;
  onClearFilter: () => void;
}

const JobsListFilter: React.SFC<Props> = ({
  jobListingsFilter,
  onUpdateFilter,
  onClearFilter
}) => {
  return (
    <Paper>
      <Typography variant="h5">Filter</Typography>
    </Paper>
  );
};

export default JobsListFilter;
