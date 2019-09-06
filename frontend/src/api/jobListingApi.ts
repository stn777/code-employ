import { postApi } from "./apiUtils";
import {
  JobListingSearchResponse,
  JobListingSearchFilter
} from "../common/types";

const baseUrl = process.env.API_URL + "/job-listing";

export async function searchJobListings(
  filter: JobListingSearchFilter
): Promise<JobListingSearchResponse> {
  return await postApi<JobListingSearchResponse>(
    `${baseUrl}/paged`,
    filter
  ).catch(error => {
    throw new Error(error);
  });
}
