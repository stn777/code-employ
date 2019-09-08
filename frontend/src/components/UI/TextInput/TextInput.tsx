import * as React from "react";
import { TextField } from "@material-ui/core";

interface Props {
  name: string;
  value: string;
  type?: string;
  label?: string;
  placeholder?: string;
  onChange?: (e: any) => void;
}

const TextInput: React.SFC<Props> = ({
  name,
  type,
  label,
  value,
  placeholder,
  onChange
}) => (
  <TextField
    name={name}
    type={type}
    label={label}
    value={value}
    placeholder={placeholder}
    onChange={onChange}
  />
);

export default TextInput;
