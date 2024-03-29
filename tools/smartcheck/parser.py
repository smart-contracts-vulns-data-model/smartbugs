import sb.parse_utils

VERSION = "2022/11/14"

FINDINGS = {
    "SOLIDITY_ADDRESS_HARDCODED",
    "SOLIDITY_ARRAY_LENGTH_MANIPULATION",
    "SOLIDITY_BALANCE_EQUALITY",
    "SOLIDITY_BYTE_ARRAY_INSTEAD_BYTES",
    "SOLIDITY_CONSTRUCTOR_RETURN",
    "SOLIDITY_CALL_WITHOUT_DATA",
    "SOLIDITY_DELETE_ON_DYNAMIC_ARRAYS",
    "SOLIDITY_DEPRECATED_CONSTRUCTIONS",
    "SOLIDITY_DIV_MUL",
    "SOLIDITY_DO_WHILE_CONTINUE",
    "SOLIDITY_DOS_WITH_THROW",
    "SOLIDITY_ERC20_APPROVE",
    "SOLIDITY_ERC20_FUNCTIONS_ALWAYS_RETURN_FALSE",
    "SOLIDITY_ERC20_INDEXED",
    "SOLIDITY_ERC20_TRANSFER_SHOULD_THROW",
    "SOLIDITY_EXACT_TIME",
    "SOLIDITY_EXTRA_GAS_IN_LOOPS",
    "SOLIDITY_FUNCTION_RETURNS_TYPE_AND_NO_RETURN",
    "SOLIDITY_FUNCTIONS_RETURNS_TYPE_AND_NO_RETURN",
    "SOLIDITY_GAS_LIMIT_IN_LOOPS",
    "SOLIDITY_INCORRECT_BLOCKHASH",
    "SOLIDITY_LOCKED_MONEY",
    "SOLIDITY_MSGVALUE_EQUALS_ZERO",
    "SOLIDITY_OVERPOWERED_ROLE",
    "SOLIDITY_PRAGMAS_VERSION",
    "SOLIDITY_PRIVATE_MODIFIER_DOES_NOT_HIDE_DATA",
    "SOLIDITY_PRIVATE_MODIFIER_DONT_HIDE_DATA",
    "SOLIDITY_REDUNDANT_FALLBACK_REJECT",
    "SOLIDITY_REVERT_REQUIRE",
    "SOLIDITY_REWRITE_ON_ASSEMBLY_CALL",
    "SOLIDITY_SAFEMATH",
    "SOLIDITY_SEND",
    "SOLIDITY_SHOULD_NOT_BE_PURE",
    "SOLIDITY_SHOULD_NOT_BE_VIEW",
    "SOLIDITY_SHOULD_RETURN_STRUCT",
    "SOLIDITY_TRANSFER_IN_LOOP",
    "SOLIDITY_TX_ORIGIN",
    "SOLIDITY_UINT_CANT_BE_NEGATIVE",
    "SOLIDITY_UNCHECKED_CALL",
    "SOLIDITY_UNUSED_FUNCTION_SHOULD_BE_EXTERNAL",
    "SOLIDITY_UPGRADE_TO_050",
    "SOLIDITY_USING_INLINE_ASSEMBLY",
    "SOLIDITY_VAR",
    "SOLIDITY_VAR_IN_LOOP_FOR",
    "SOLIDITY_VISIBILITY",
    "SOLIDITY_WRONG_SIGNATURE",
}

def parse(exit_code, log, output):
    findings, infos = [], set()
    errors, fails = sb.parse_utils.errors_fails(exit_code, log)

    for line in log:
        i = line.find(": ")
        if i >= 0:
            k = line[0:i].strip()
            v = line[i+2:].strip()
            if v.isdigit():
                v = int(v)
            if k.endswith("ruleId"):
                finding = { "name": v }
                findings.append(finding)
            elif k in ("severity", "line", "column"):
                finding[k] = v

    return findings, infos, errors, fails
