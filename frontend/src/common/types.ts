export interface JobListing {
  id: number;
  jobTitle: string;
  description: string;
  positionType: number;
  contractLength: number;
  salary: number;
  salaryFrequency: number;
  city: string;
  postCode: string;
  status: number;
  closedDate: Date;
  createdDate: Date;
  modifiedDate: Date;
}

export interface JobListingSearchResponse {
  recordCount: number;
  items: JobListing[];
}

export interface NavBarItem {
  label: string;
  route: string;
}
