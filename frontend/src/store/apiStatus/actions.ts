import {
  BEGIN_API_CALL,
  API_CALL_ERROR,
  BeginApiCall,
  ApiCallError
} from "./types";

export const beginApiCall = (): BeginApiCall => {
  return {
    type: BEGIN_API_CALL
  };
};

export const apiCallError = (): ApiCallError => {
  return {
    type: API_CALL_ERROR
  };
};
