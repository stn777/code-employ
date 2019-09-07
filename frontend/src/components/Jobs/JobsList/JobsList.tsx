import * as React from "react";
import { JobListingSearchResponse, JobListing } from "../../../common/types";
import JobsListItem from "../JobsListItem";
import { Grid, Typography } from "@material-ui/core";

interface Props {
  jobListings: JobListingSearchResponse;
}

const JobsList: React.SFC<Props> = ({ jobListings }) => {
  const { recordCount, items } = jobListings;
  return (
    <>
      <Typography>
        Showing {items.length} of {recordCount}
      </Typography>
      <Grid container spacing={3}>
        {items.map(job => {
          return (
            <Grid key={job.id} item xs={12}>
              <JobsListItem jobListing={job} />
            </Grid>
          );
        })}
      </Grid>
    </>
  );
};

export default JobsList;
