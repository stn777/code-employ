import * as React from "react";
import * as styles from "./styles.module.scss";

export interface HelloProps {}

// 'HelloProps' describes the shape of props.
// State is never set so we use the '{}' type.
export class Hello extends React.Component<HelloProps, {}> {
  render() {
    return <div className={styles.root}>Hello world</div>;
  }
}
