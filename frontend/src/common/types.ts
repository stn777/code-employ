export interface LocationCountryCode {
  id: number;
  name: string;
  code: string;
}

export interface LocationStateCode {
  id: number;
  name: string;
  code: string;
}

export interface ProgrammingLanguage {
  id: number;
  name: string;
}

export interface Tag {
  id: number;
  title: string;
}

export interface Company {
  id: number;
  legalName: string;
  email: string;
  websiteUrl: string;
  city: string;
  country: LocationCountryCode;
  state: LocationStateCode;
  postCode: string;
  createdDate: Date;
}

export interface JobListing {
  id: number;
  jobTitle: string;
  description: string;
  company: Company;
  positionType: number;
  contractLength: number;
  salary: number;
  salaryFrequency: number;
  city: string;
  country: LocationCountryCode;
  state: LocationStateCode;
  postCode: string;
  status: number;
  languages: ProgrammingLanguage[];
  tags: Tag[];
  closedDate: Date;
  createdDate: Date;
  modifiedDate: Date;
}

export interface JobListingList {
  id: number;
  companyName: string;
  jobTitle: string;
  description: string;
  positionType: string;
  contractLength: number;
  salary: number;
  salaryFrequency: string;
  languages: string[];
  city: string;
  stateName: string;
  countryName: string;
  postCode: string;
  tags: string[];
  createdDate: Date;
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
  items: JobListingList[];
}

export interface NavBarItem {
  label: string;
  route: string;
}
