import * as React from "react";
import { JobListingSearchResponse } from "../../../common/types";

interface Props {
  jobListings: JobListingSearchResponse;
}

export const JobsList: React.SFC<Props> = ({ jobListings }) => {
  const { recordCount, items } = jobListings;
  return (
    <div>
      <p>Total records: {recordCount}</p>
      <ul>
        {items.map(job => {
          return <li key={job.id}>{job.jobTitle}</li>;
        })}
      </ul>
    </div>
  );
};
