export const BEGIN_API_CALL = "BEGIN_API_CALL";
export const API_CALL_ERROR = "API_CALL_ERROR";

export interface ApiStatusState {
  apiCallsInProgress: number;
}

export interface BeginApiCall {
  type: typeof BEGIN_API_CALL;
}

export interface ApiCallError {
  type: typeof API_CALL_ERROR;
}
