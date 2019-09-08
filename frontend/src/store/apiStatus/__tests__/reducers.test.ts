import apiStatusReducer from "../reducers";
import * as actions from "../actions";
import { ApiStatusState } from "../types";

it("should increment the amount of apiCallsInProgress when passed BEGIN_API_CALL", () => {
  const initialState: ApiStatusState = {
    apiCallsInProgress: 0
  };

  const action = actions.beginApiCall();
  const newState = apiStatusReducer(initialState, action);

  expect(newState.apiCallsInProgress).toEqual(1);
});

it("should decrement the amount of apiCallsInProgress when passed any SUCCESS action", () => {
  const initialState: ApiStatusState = {
    apiCallsInProgress: 1
  };

  const action = { type: "TEST_SUCCESS" };
  const newState = apiStatusReducer(initialState, action);

  expect(newState.apiCallsInProgress).toEqual(0);
});

it("should decrement the amount of apiCallsInProgress when passed API_CALL_ERROR", () => {
  const initialState: ApiStatusState = {
    apiCallsInProgress: 1
  };

  const action = actions.apiCallError();
  const newState = apiStatusReducer(initialState, action);

  expect(newState.apiCallsInProgress).toEqual(0);
});
