import * as React from "react";
import { JobListingSearchFilter } from "../../../common/types";
import { Paper, Typography, Grid, Box } from "@material-ui/core";
import TextInput from "../../UI/TextInput";

interface Props {
  jobListingsFilter: JobListingSearchFilter;
  onUpdateFilter: (e: any) => void;
  onClearFilter: () => void;
}

const JobsListFilter: React.SFC<Props> = ({
  jobListingsFilter,
  onUpdateFilter,
  onClearFilter
}) => {
  return (
    <Paper>
      <Box p={3}>
        <Typography variant="h5">Filter</Typography>
        <Box py={3}>
          <TextInput
            label="Keyword"
            value={jobListingsFilter.keyword}
            placeholder="Enter a keyword..."
            onChange={onUpdateFilter}
          />
        </Box>
      </Box>
    </Paper>
  );
};

export default JobsListFilter;
