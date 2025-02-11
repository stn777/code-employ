import * as React from "react";
import { Card, CardHeader, CardContent, Typography } from "@material-ui/core";
import { JobListingList } from "../../../common/types";

interface Props {
  jobListing: JobListingList;
}

const JobsListItem: React.SFC<Props> = ({ jobListing }) => {
  return (
    <Card>
      <CardHeader
        title={jobListing.jobTitle}
        subheader={jobListing.companyName}
      />
      <CardContent>
        <Typography variant="body1" color="textPrimary" component="p">
          {jobListing.city}, {jobListing.stateName}
        </Typography>
        <Typography variant="body1" color="textSecondary" component="p">
          {jobListing.description}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default JobsListItem;
