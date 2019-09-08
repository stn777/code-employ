import { BEGIN_API_CALL, API_CALL_ERROR, ApiStatusState } from "./types";

const actionTypeEndsInSuccess = (type: any) =>
  type.substring(type.length - 8) === "_SUCCESS";

const initialState: ApiStatusState = {
  apiCallsInProgress: 0
};

export default function apiStatusReducer(
  state: ApiStatusState = initialState,
  action: any
): ApiStatusState {
  if (action.type == BEGIN_API_CALL) {
    return {
      apiCallsInProgress: state.apiCallsInProgress + 1
    };
  } else if (
    action.type === API_CALL_ERROR ||
    actionTypeEndsInSuccess(action.type)
  ) {
    return {
      apiCallsInProgress: state.apiCallsInProgress - 1
    };
  }
  return state;
}
