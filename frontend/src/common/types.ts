export interface JobListing {
  job_title: string;
  description: string;
  position_type: number;
  contract_length: number;
  salary: number;
  salary_frequency: number;
  city: string;
  post_code: string;
  status: number;
  closed_date: Date;
  created_date: Date;
  modified_date: Date;
}

export interface JobListingSearchResponse {
  record_count: number;
  items: JobListing[];
}
