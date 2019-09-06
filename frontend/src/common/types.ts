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

export interface PaginationFilter {
  currentPage: number;
  itemsPerPage: number;
  orderByColumn: string;
  orderDirection: boolean;
}

export interface PagedResponse {
  recordCount: number;
}

export interface JobListingSearchFilter extends PaginationFilter {
  keyword: string;
  languages: number[];
  positionType: number;
  salaryMin: number;
  salaryMax: number;
}

export interface JobListingSearchResponse extends PagedResponse {
  items: JobListing[];
}

export interface NavBarItem {
  label: string;
  route: string;
}
