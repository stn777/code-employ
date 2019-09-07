import * as React from "react";
import { Card, CardHeader, CardContent, Typography } from "@material-ui/core";
import { JobListing } from "../../../common/types";

interface Props {
  jobListing: JobListing;
}

const JobsListItem: React.SFC<Props> = ({ jobListing }) => {
  const { state } = jobListing;
  return (
    <Card>
      <CardHeader
        title={jobListing.jobTitle}
        subheader={`${jobListing.city}, ${state.name}`}
      />
      <CardContent>
        <Typography variant="body1" color="textSecondary" component="p">
          {jobListing.description}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default JobsListItem;
