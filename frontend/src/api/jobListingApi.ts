import { postApi } from "./apiUtils";
import { JobListingSearchResponse } from "../common/types";

const baseUrl = process.env.API_URL + "/job-listing";

export async function searchJobListings(
  filter: any
): Promise<JobListingSearchResponse> {
  return await postApi<JobListingSearchResponse>(
    `${baseUrl}/paged`,
    filter
  ).catch(error => {
    throw new Error(error);
  });
}
