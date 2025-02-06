class Blueprint:
    """This is a small class without any practical use case.

    This class has no useful functionality apart from learning how to write
    documentation for a class.

    Parameters
    ----------
    count : numbers.real

        Number of items.

    participants : numbers.real

        Number of participants. Must be larger than zero.

    name : str

        Task name. Defaults to ``standard``.

    Raises
    ------
    ValueError
        If ``participants`` is not larger than zero.

    Examples
    --------
    >>> from blaupause import Blueprint
    >>> bp = Blueprint(count=3, participants=1)
    >>> bp
    Blueprint(count=3, participants=1, name=standard)
    """

    def __init__(self, count, participants, name='standard'):
        self.count = count
        self.participants = participants
        self.name = name

    @property
    def participants(self):
        '''Number of participants.'''
        return self._participants

    @participants.setter
    def participants(self, participants):
        '''Participant number must be larger than zero.'''
        if participants > 0:
            self._participants = participants
        else:
            raise ValueError('``participants`` mus be larger than zero')

    @property
    def shares(self):
        '''Divide a and b.

        Returns
        -------
        numbers.real

            a / b

        Examples
        --------
        >>> from blaupause import Blueprint
        >>> bp = Blueprint(count=6, participants=2)
        >>> bp.shares
        3.0
        '''
        return self.count / self.participants

    def mean_shares(self, value):
        '''Mean of the given value and class properties.

        This method computes the mean of the given value and the two
        values ``a`` and ``b`` of the current instance of ``MyClass``.

        Parameters
        ----------

        value : numbers.real

            Third value to compute mean with.

        Returns
        -------
        numbers.real

            The mean.

        Examples
        --------
        >>> from blaupause import Blueprint
        >>> bp = Blueprint(count=2, participants=3)
        >>> bp.mean_shares(4)
        2.0
        '''
        sum = self.count + value
        return sum / self.participants

    def do_nothing(self):
        '''Method that does nothing.

        This method does not do anything. Its only purpose is to have
        more methods in the documentation.
        '''
        pass

    def __add__(self, other):
        '''
        Add two instances of ``MyClass``
        '''
        if not isinstance(other, self.__class__):
            msg = f'Cannot add objects of {type(self)=} and {type(other)=}'
            raise TypeError(msg)
        count = self.count + other.count
        participants = self.participants + other.b
        name = self._join_names([self.name, other.name])
        return self.__class__(count=count, participants=participants,
                              name=name)

    def __radd__(self, other):
        '''Operator +=
        '''
        self.count += other.count
        self.participants += other.participants
        self.name = self._join_names([self.name, other.name])

    def _join_names(self, names):
        return '|'.join(names)

    def __repr__(self):
        return (f'Blueprint(count={self.count}, '
                f'participants={self.participants}, '
                f'name={self.name})')

    @staticmethod
    def print_blueprint():
        '''Prints ``blueprint``.

        This method only prints the word ``blueprint``.
        Used to have a static method in the documentation.
        '''
        print('blueprint')
