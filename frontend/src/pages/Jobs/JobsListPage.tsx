import * as React from "react";
import { JobsListContainer as JobsList } from "../../components/Jobs/JobsList";
import { Grid } from "@material-ui/core";

const JobsListPage = () => (
  <div>
    <Grid item>
      <h1>Available Jobs</h1>
      <JobsList />
    </Grid>
  </div>
);

export default JobsListPage;
