# taken from :
# pathlib : https://github.com/python/typeshed/blob/master/stdlib/3/pathlib.pyi
# OpenBinaryMode..., OpenTextMode, StrPath from https://raw.githubusercontent.com/python/typeshed/master/stdlib/2and3/_typeshed/__init__.pyi
# shutil from https://github.com/python/typeshed/blob/master/stdlib/2and3/shutil.pyi

import os
import sys
from types import TracebackType
from typing import IO, Any, BinaryIO, Callable, Generator, Iterable, List, Literal, Optional, Sequence, TextIO, Tuple, Type, TypeVar, Union, overload
from os import PathLike
StrPath = Union[str, PathLike[str]]

OpenBinaryModeUpdating = Literal[
    "rb+",
    "r+b",
    "+rb",
    "br+",
    "b+r",
    "+br",
    "wb+",
    "w+b",
    "+wb",
    "bw+",
    "b+w",
    "+bw",
    "ab+",
    "a+b",
    "+ab",
    "ba+",
    "b+a",
    "+ba",
    "xb+",
    "x+b",
    "+xb",
    "bx+",
    "b+x",
    "+bx",
]

OpenBinaryModeReading = Literal[
    "rb", "br", "rbU", "rUb", "Urb", "brU", "bUr", "Ubr",
]

OpenBinaryModeWriting = Literal[
    "wb", "bw", "ab", "ba", "xb", "bx",
]

OpenBinaryMode = Union[OpenBinaryModeUpdating, OpenBinaryModeReading, OpenBinaryModeWriting]

OpenTextMode = Literal[
    "r",
    "r+",
    "+r",
    "rt",
    "tr",
    "rt+",
    "r+t",
    "+rt",
    "tr+",
    "t+r",
    "+tr",
    "w",
    "w+",
    "+w",
    "wt",
    "tw",
    "wt+",
    "w+t",
    "+wt",
    "tw+",
    "t+w",
    "+tw",
    "a",
    "a+",
    "+a",
    "at",
    "ta",
    "at+",
    "a+t",
    "+at",
    "ta+",
    "t+a",
    "+ta",
    "x",
    "x+",
    "+x",
    "xt",
    "tx",
    "xt+",
    "x+t",
    "+xt",
    "tx+",
    "t+x",
    "+tx",
    "U",
    "rU",
    "Ur",
    "rtU",
    "rUt",
    "Urt",
    "trU",
    "tUr",
    "Utr",
]

_P = TypeVar("_P", bound=PurePath)

if sys.version_info >= (3, 6):
    _PurePathBase = os.PathLike[str]
else:
    _PurePathBase = object

class PurePath(_PurePathBase):
    parts: Tuple[str, ...]
    drive: str
    root: str
    anchor: str
    name: str
    suffix: str
    suffixes: List[str]
    stem: str
    if sys.version_info < (3, 5):
        def __init__(self, *pathsegments: str) -> None: ...
    elif sys.version_info < (3, 6):
        def __new__(cls: Type[_P], *args: Union[str, PurePath]) -> _P: ...
    else:
        def __new__(cls: Type[_P], *args: Union[str, os.PathLike[str]]) -> _P: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: PurePath) -> bool: ...
    def __le__(self, other: PurePath) -> bool: ...
    def __gt__(self, other: PurePath) -> bool: ...
    def __ge__(self, other: PurePath) -> bool: ...
    if sys.version_info < (3, 6):
        def __truediv__(self: _P, key: Union[str, PurePath]) -> _P: ...
        def __rtruediv__(self: _P, key: Union[str, PurePath]) -> _P: ...
    else:
        def __truediv__(self: _P, key: Union[str, os.PathLike[str]]) -> _P: ...
        def __rtruediv__(self: _P, key: Union[str, os.PathLike[str]]) -> _P: ...
    if sys.version_info < (3,):
        def __div__(self: _P, key: Union[str, PurePath]) -> _P: ...
    def __bytes__(self) -> bytes: ...
    def as_posix(self) -> str: ...
    def as_uri(self) -> str: ...
    def is_absolute(self) -> bool: ...
    def is_reserved(self) -> bool: ...
    if sys.version_info >= (3, 9):
        def is_relative_to(self, *other: Union[str, os.PathLike[str]]) -> bool: ...
    def match(self, path_pattern: str) -> bool: ...
    if sys.version_info < (3, 6):
        def relative_to(self: _P, *other: Union[str, PurePath]) -> _P: ...
    else:
        def relative_to(self: _P, *other: Union[str, os.PathLike[str]]) -> _P: ...
    def with_name(self: _P, name: str) -> _P: ...
    if sys.version_info >= (3, 9):
        def with_stem(self: _P, stem: str) -> _P: ...
    def with_suffix(self: _P, suffix: str) -> _P: ...
    if sys.version_info < (3, 6):
        def joinpath(self: _P, *other: Union[str, PurePath]) -> _P: ...
    else:
        def joinpath(self: _P, *other: Union[str, os.PathLike[str]]) -> _P: ...
    @property
    def parents(self: _P) -> Sequence[_P]: ...
    @property
    def parent(self: _P) -> _P: ...
    def append_suffix(self: _P, suffix: str) -> _P: ...
    if sys.version_info < (3, 6):
        def joinpath(self: _P, *other: Union[str, PurePath]) -> _P: ...
    else:
        def joinpath(self: _P, *other: Union[str, os.PathLike[str]]) -> _P: ...
    def replace_parts(self: _P, old: _P, new: _P) -> _P: ...

class PurePosixPath(PurePath): ...
class PureWindowsPath(PurePath): ...

class Path(PurePath):
    def __enter__(self) -> Path: ...
    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]
    ) -> Optional[bool]: ...
    @classmethod
    def cwd(cls: Type[_P]) -> _P: ...
    def stat(self) -> os.stat_result: ...
    def chmod(self, mode: int) -> None: ...
    def exists(self) -> bool: ...
    def glob(self, pattern: str) -> Generator[Path, None, None]: ...
    def group(self) -> str: ...
    def is_dir(self) -> bool: ...
    def is_file(self) -> bool: ...
    if sys.version_info >= (3, 7):
        def is_mount(self) -> bool: ...
    def is_symlink(self) -> bool: ...
    def is_socket(self) -> bool: ...
    def is_fifo(self) -> bool: ...
    def is_block_device(self) -> bool: ...
    def is_char_device(self) -> bool: ...
    def iterdir(self) -> Generator[Path, None, None]: ...
    def lchmod(self, mode: int) -> None: ...
    def lstat(self) -> os.stat_result: ...
    if sys.version_info < (3, 5):
        def mkdir(self, mode: int = ..., parents: bool = ...) -> None: ...
    else:
        def mkdir(self, mode: int = ..., parents: bool = ..., exist_ok: bool = ...) -> None: ...
    @overload
    def open(
        self,
        mode: OpenTextMode = ...,
        buffering: int = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
    ) -> TextIO: ...
    @overload
    def open(
        self, mode: OpenBinaryMode, buffering: int = ..., encoding: None = ..., errors: None = ..., newline: None = ...
    ) -> BinaryIO: ...
    @overload
    def open(
        self,
        mode: str,
        buffering: int = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
    ) -> IO[Any]: ...
    def owner(self) -> str: ...
    if sys.version_info >= (3, 9):
        def readlink(self: _P) -> _P: ...
    if sys.version_info >= (3, 8):
        def rename(self: _P, target: Union[str, PurePath]) -> _P: ...
        def replace(self: _P, target: Union[str, PurePath]) -> _P: ...
    else:
        def rename(self, target: Union[str, PurePath]) -> None: ...
        def replace(self, target: Union[str, PurePath]) -> None: ...
    if sys.version_info < (3, 6):
        def resolve(self: _P) -> _P: ...
    else:
        def resolve(self: _P, strict: bool = ...) -> _P: ...
    def rglob(self, pattern: str) -> Generator[Path, None, None]: ...
    def rmdir(self) -> None: ...
    def symlink_to(self, target: Union[str, Path], target_is_directory: bool = ...) -> None: ...
    def touch(self, mode: int = ..., exist_ok: bool = ...) -> None: ...
    if sys.version_info >= (3, 8):
        def unlink(self, missing_ok: bool = ...) -> None: ...
    else:
        def unlink(self) -> None: ...
    if sys.version_info >= (3, 5):
        @classmethod
        def home(cls: Type[_P]) -> _P: ...
        if sys.version_info < (3, 6):
            def __new__(cls: Type[_P], *args: Union[str, PurePath], **kwargs: Any) -> _P: ...
        else:
            def __new__(cls: Type[_P], *args: Union[str, os.PathLike[str]], **kwargs: Any) -> _P: ...
        def absolute(self: _P) -> _P: ...
        def expanduser(self: _P) -> _P: ...
        def read_bytes(self) -> bytes: ...
        def read_text(self, encoding: Optional[str] = ..., errors: Optional[str] = ...) -> str: ...
        def samefile(self, other_path: Union[str, bytes, int, Path]) -> bool: ...
        def write_bytes(self, data: bytes) -> int: ...
        def write_text(self, data: str, encoding: Optional[str] = ..., errors: Optional[str] = ...) -> int: ...
    if sys.version_info >= (3, 8):
        def link_to(self, target: Union[str, bytes, os.PathLike[str]]) -> None: ...
    def copy(self: _P, target: PurePath, follow_symlinks: bool = ...) -> None: ...
    def copy2(self: _P, target: PurePath, follow_symlinks: bool = ...) -> None: ...
    def copyfile(self: _P, target: PurePath, follow_symlinks: bool = ...) -> None: ...
    def copymode(self: _P, target: PurePath, follow_symlinks: bool = ...) -> None: ...
    def copystat(self: _P, target: PurePath, follow_symlinks: bool = ...) -> None: ...
    def copytree(self: _P,
                 target: PurePath,
                 symlinks: bool = ...,
                 follow_symlinks: bool = ...,
                 ignore: Union[None, Callable[[str, List[str]], Iterable[str]], Callable[[StrPath, List[str]], Iterable[str]]] = ...,
                 copy_function: Callable[[str, str], None] = ...,
                 ignore_dangling_symlinks: bool = ...,
                 dirs_exist_ok: bool = ...,
                 ) -> None: ...
    def rmtree(self: _P,  ignore_errors: bool = ..., onerror: Optional[Callable[[Any, Any, Any], Any]] = ...) -> None: ...

class PosixPath(Path, PurePosixPath): ...
class WindowsPath(Path, PureWindowsPath): ...