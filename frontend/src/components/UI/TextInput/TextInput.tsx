import * as React from "react";
import { TextField } from "@material-ui/core";

interface Props {
  type?: string;
  label?: string;
  value: string;
  placeholder?: string;
  onChange?: (e: any) => void;
}

const TextInput: React.SFC<Props> = ({
  type,
  label,
  value,
  placeholder,
  onChange
}) => (
  <TextField
    type={type}
    label={label}
    value={value}
    placeholder={placeholder}
    onChange={onChange}
  />
);

export default TextInput;
