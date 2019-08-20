import * as React from 'react';
import Button from '@material-ui/core/Button'
import * as styles from './styles.module.scss';

export interface HelloProps { }

// 'HelloProps' describes the shape of props.
// State is never set so we use the '{}' type.
export class Hello extends React.Component<HelloProps, {}> {
    render() {
        return (
            <Button variant="contained" color="primary">
                Material UI
            </Button>
        );
    }
}
