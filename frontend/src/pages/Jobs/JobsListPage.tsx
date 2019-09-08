import * as React from "react";
import { JobsListContainer as JobsList } from "../../components/Jobs/JobsList";
import { JobsListFilterContainer as JobsListFilter } from "../../components/Jobs/JobsListFilter";
import { Grid, Typography } from "@material-ui/core";

const JobsListPage = () => (
  <div>
    <Grid container spacing={3}>
      <Grid item xs={3}>
        <JobsListFilter />
      </Grid>
      <Grid item xs={9}>
        <Typography variant="h4">Available Jobs</Typography>
        <JobsList />
      </Grid>
    </Grid>
  </div>
);

export default JobsListPage;
