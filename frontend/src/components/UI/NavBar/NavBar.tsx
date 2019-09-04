import * as React from "react";
import { List, ListItem, ListItemText, Link } from "@material-ui/core";
import TypoGraphy from "@material-ui/core/Typography";
import { Link as RouterLink } from "react-router-dom";
import { NavBarItem } from "../../../common/types";

interface Props {
  navItems: NavBarItem[];
}

const NavBar: React.SFC<Props> = ({ navItems }) => (
  <List component="nav">
    <ListItem component="div">
      {navItems.map(item => {
        return (
          <ListItemText inset>
            <TypoGraphy variant="h6">
              <Link color="inherit" component={RouterLink} to={item.route}>
                {item.label}
              </Link>
            </TypoGraphy>
          </ListItemText>
        );
      })}
    </ListItem>
  </List>
);

export default NavBar;
